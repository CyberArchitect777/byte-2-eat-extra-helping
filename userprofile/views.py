# Ensures only logged-in users will see this page
from django.contrib.auth.decorators import login_required
# Shortcut for rendering a template and returning an HTTP response
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy  # Handles URL redirection
from index.models import Review  # Import Review model
from index.forms import ReviewForm  # Import Review form

# User dashboard that shows all their reviews
@login_required
def takeaway_dashboard(request):
    allowed_sort_fields = [
        "takeaway_name", "food_type", "rating", "created_on"
    ]
    allowed_direction_field = "sort_order"

    user_reviews = Review.objects.filter(poster=request.user)

    if request.method == "GET":
        selected_sort = request.GET.get("sort_by", "created_on")
        selected_direction = request.GET.get("sort_order", "asc")
        if selected_sort in allowed_sort_fields:
            direction_symbol = ""
            if selected_direction == "desc":
                direction_symbol = "-"
            user_reviews = user_reviews.order_by(
                direction_symbol + selected_sort
            )

    return render(
        request,
        "userprofile/takeaway_dashboard.html",
        {
            "user_reviews": user_reviews,
        }
    )

# Add a review
def add_review(request, review_id=None):
    # Checks that a valid user is logged in. If not, users will be redirected to the login page.
    if not request.user.is_authenticated:
        return redirect(reverse("account_login"))

    if review_id:  # Checks to see if review_id is provided
        review = get_object_or_404(Review, id=review_id)
        # If there is a review_id, then the form will populate with data from
        # that existing review
    else:
        # If there is no review_id, then the form will be blank/new and ready
        # to be filled in
        review = None

    # This block handles the form submission
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():  # Checks if form's validation rules are met
            review = form.save(commit=False)  # Doesn't commit form to the
            # database yet
            review.poster = request.user  # Assigns the logged-in user to the
            # review
            review.save()  # Now saves form to the database
            return redirect("takeaway_dashboard")  # Redirects User to dashboard
            # with all their reviews

    # This block handles the GET requests and displays the form
    else:
        form = ReviewForm(instance=review)  # Empty form for user to fill in

    # This block renders the form template
    return render(
        request,
        "userprofile/add_review.html",
        {"form": form, "review": review}
    )

# Edit a review
@login_required
def edit_review(request, pk):
    try:
        review = Review.objects.get(pk=pk)
    except Review.DoesNotExist as e:
        return redirect("takeaway_dashboard")  # Redirects User to dashboard if review being edited doesn't exist
    if request.method == "POST": # Form to database handling code if review is actually being submitted for edit
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review.save()
        return redirect("takeaway_dashboard")
    else: # If the editing submission process is not underway
        if request.user == review.poster: # Check to see if the current user matches the review posters (essential for security)
            form = ReviewForm(instance=review)
        else:
            return redirect("takeaway_dashboard") # Return to dashboard if not
    return render(
        request,
        "userprofile/edit_review.html",
        {"form": form, "review": review}
    )

# Delete a review
@login_required
def delete_review(request, pk):
    try:
        review = Review.objects.get(pk=pk)
    except Review.DoesNotExist as e:
        return redirect("takeaway_dashboard")
    if review.poster == request.user: # Only delete the review if the user logged in is the one who wrote the review
        review.delete()
    return redirect("takeaway_dashboard")  # Redirects User to dashboard
