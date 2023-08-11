from django.db.models.signals import post_save, pre_delete, pre_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Profile, Company, Education
import os
from django.conf import settings

user = get_user_model()

@receiver(post_save, sender=user)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if not instance.role:  # access the field of instance
            p = Profile.objects.create(
                user=instance)  # you have correctly passed instance to foreign key and you just need to check condition for the same
        else:
            p = Company.objects.create(user=instance)


@receiver(post_save, sender=user)
def save_profile(sender, instance, **kwargs):
    if not instance.role:
        instance.profile.save()
    else:
        instance.company.save()


@receiver(pre_save, sender=Profile)
def auto_delete_file_on_change_profile(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `Profile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_photo = Profile.objects.get(pk=instance.pk).photo
    except Profile.DoesNotExist:
        return False

    new_photo = instance.photo
    if not old_photo == new_photo:
        try:
            if os.path.isfile(old_photo.path):
                os.remove(old_photo.path)
        except:
            return False


@receiver(pre_save, sender=Company)
def auto_delete_file_on_change_company(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `Company` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_logo = Company.objects.get(pk=instance.pk).logo
    except Company.DoesNotExist:
        return False

    new_logo = instance.logo
    if not old_logo == new_logo:
        try:
            if os.path.isfile(old_logo.path):
                os.remove(old_logo.path)
        except:
            return False


@receiver(pre_save, sender=Education)
def auto_delete_file_on_change_education(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `Education` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Education.objects.get(pk=instance.pk).diploma_certificate
    except Education.DoesNotExist:
        print('edu not exist')
        return False

    new_file = instance.diploma_certificate
    if not old_file == new_file:
        try:
            if os.path.isfile(old_file.path):
                os.remove(old_file.path)
        except:
            return False

