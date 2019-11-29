from django import forms
from .models import Object, Comment, Restaurant, SportFitness, CarService, BeautySalon, FastFood, CarWash, Fun, Other
from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            'title',
            'content',
            'city',
            'address',
            'phone',
            'email',
            'site',
            'facebook',
            'instagram',
            'seats',
            'bulgarian_kitchen',
            'italian_kitchen',
            'french_kitchen',
            'is_garden',
            'is_playground'

        ]

class SportFitnessForm(forms.ModelForm):
    class Meta:
        model = SportFitness
        fields = [
            'title',
            'content',
            'city',
            'address',
            'phone',
            'email',
            'site',
            'facebook',
            'instagram',
            'is_fitness_trainer',
        ]

class BeautySalonForm(forms.ModelForm):
    class Meta:
        model = BeautySalon
        fields = [
            'title',
            'content',
            'city',
            'address',
            'phone',
            'email',
            'site',
            'facebook',
            'instagram',
            'is_hair_salon',
            'is_laser_epilation'
        ]

class CarServiceForm(forms.ModelForm):
    class Meta:
        model = CarService
        fields = [
            'title',
            'content',
            'city',
            'address',
            'phone',
            'email',
            'site',
            'facebook',
            'instagram',
            'is_parts_clients',
        ]

class FastFoodForm(forms.ModelForm):
    class Meta:
        model = FastFood
        fields = [
            'title',
            'content',
            'city',
            'address',
            'phone',
            'email',
            'site',
            'facebook',
            'instagram',
            'is_pizza',
            'is_duner',
            'is_seats',
        ]

class CarWashForm(forms.ModelForm):
    class Meta:
        model = CarWash
        fields = [
            'title',
            'content',
            'city',
            'address',
            'phone',
            'email',
            'site',
            'facebook',
            'instagram',
            'is_external_cleaning',
            'is_internal_cleaning',
            'is_engine_cleaning',
        ]

class FunForm(forms.ModelForm):
    class Meta:
        model = Fun
        fields = [
            'title',
            'content',
            'city',
            'address',
            'phone',
            'email',
            'site',
            'facebook',
            'instagram',
            'is_working_weekend',
            'is_kids_suitable',
        ]

class OtherForm(forms.ModelForm):
    class Meta:
        model = Other
        fields = [
            'title',
            'content',
            'city',
            'address',
            'phone',
            'email',
            'site',
            'facebook',
            'instagram',
            'is_working_weekend'
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content',
        ]




class UploadForm(forms.Form):
    attachments = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)

    # If you need to upload media files, you can use this:
    attachments = MultiMediaField(
        min_num=1,
        max_num=3,
        max_file_size=1024*1024*5,
        media_type='video'  # 'audio', 'video' or 'image'
    )

    # For images (requires Pillow for validation):
    attachments = MultiImageField(min_num=1, max_num=3, max_file_size=1024*1024*5)