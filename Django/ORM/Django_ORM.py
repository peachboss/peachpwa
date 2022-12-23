from django.db import models

class UserData(models.Model):
    UserID = models.IntegerField(primary_key=True)
    Username = models.CharField(max_length=255)
    Pin = models.IntegerField()
    SubscriptionTier = models.CharField(max_length=255)
    Friends = models.ArrayField(
        models.IntegerField()
    )
    VideoIDsViewed = models.ArrayField(
        models.IntegerField()
    )
    PayeeID = models.IntegerField()
    ReportCount = models.IntegerField()
    CreationDate = models.DateField()

class VideoData(models.Model):
    VideoID = models.IntegerField(primary_key=True)
    VideoURL = models.CharField(max_length=255)
    AuthorID = models.ForeignKey(
        UserData,
        on_delete=models.CASCADE,
        related_name='videos'
    )
    Category = models.CharField(max_length=255)
    UploadDate = models.DateField()
    Length = models.IntegerField()
    ViewCount = models.IntegerField()
    ChallengeID = models.ForeignKey(
        'ChallengeData',
        on_delete=models.CASCADE,
        related_name='videos',
        null=True,
        blank=True
    )
    Earnings = models.FloatField()

class PaymentData(models.Model):
    PaymentID = models.IntegerField(primary_key=True)
    UserID = models.ForeignKey(
        UserData,
        on_delete=models.CASCADE,
        related_name='payments'
    )
    Amount = models.FloatField()
    PaymentDate = models.DateField()
    PaymentMethod = models.CharField(max_length=255)

class Feed(models.Model):
    FeedID = models.IntegerField(primary_key=True)
    UserID = models.ForeignKey(
        UserData,
        on_delete=models.CASCADE,
        related_name='feeds'
    )
    VideoID = models.ForeignKey(
        VideoData,
        on_delete=models.CASCADE,
        related_name='feeds'
    )
    Date = models.DateField()

class RoomData(models.Model):
    RoomID = models.IntegerField(primary_key=True)
    HostID = models.ForeignKey(
        UserData,
        on_delete=models.CASCADE,
        related_name='hosted_rooms'
    )
    ParticipantIDs = models.ArrayField(
        models.IntegerField()
    )
    StartTime = models.DateTimeField()
    EndTime = models.DateTimeField()

class ChallengeData(models.Model):
    ChallengeID = models.IntegerField(primary_key=True)
    ChallengeName = models.CharField(max_length=255)
    StartDate = models.DateField()
    EndDate = models.DateField()

class Reports(models.Model):
    ReportID = models.IntegerField(primary_key=True)
    UserID = models.ForeignKey(
        UserData,
        on_delete=models.CASCADE,
        related_name='reports'
    )
    VideoID = models.ForeignKey(
        VideoData,
        on_delete=models.CASCADE,
        related_name='reports'
    )
    ReportReason = models.CharField(max_length=255)
    ReportDate = models.DateField() 

class Messages(models.Model):
    MessageID = models.IntegerField(primary_key=True)
    SenderID = models.ForeignKey(
        UserData,
        on_delete=models.CASCADE,
        related_name='sent_messages'
    )
    ReceiverID = models.ForeignKey(
        UserData,
        on_delete=models.CASCADE,
        related_name='received_messages'
    )
    Message = models.CharField(max_length=255)
    SendDate = models.DateField()
    ReadDate = models.DateField(null=True, blank=True)