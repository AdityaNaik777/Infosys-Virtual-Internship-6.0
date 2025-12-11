from django.contrib import admin
from .models import Category, SubCategory, QuizAttempt


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "level", "is_leaf")
    list_filter = ("category", "level", "is_leaf")
    search_fields = ("name",)


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "category", "subcategory", "score", "started_at")
    list_filter = ("category", "difficulty", "status")
