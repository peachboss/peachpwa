CREATE TABLE UserData (
  UserID INT PRIMARY KEY,
  Username VARCHAR(255),
  Pin INT,
  SubscriptionTier VARCHAR(255),
  Friends ARRAY,
  VideoIDsViewed ARRAY,
  PayeeID INT,
  ReportCount INT,
  CreationDate DATE
);

CREATE TABLE VideoData (
  VideoID INT PRIMARY KEY,
  VideoURL VARCHAR(255),
  AuthorID INT,
  FOREIGN KEY (AuthorID) REFERENCES UserData(UserID),
  Category VARCHAR(255),
  UploadDate DATE,
  Length INT,
  ViewCount INT,
  ChallengeID INT,
  FOREIGN KEY (ChallengeID) REFERENCES ChallengeData(ChallengeID),
  Earnings FLOAT
);

CREATE TABLE PaymentData (
  PaymentID INT PRIMARY KEY,
  UserID INT,
  FOREIGN KEY (UserID) REFERENCES UserData(UserID),
  Amount FLOAT,
  PaymentDate DATE,
  PaymentMethod VARCHAR(255)
);

CREATE TABLE Feed (
  FeedID INT PRIMARY KEY,
  UserID INT,
  FOREIGN KEY (UserID) REFERENCES UserData(UserID),
  VideoID INT,
  FOREIGN KEY (VideoID) REFERENCES VideoData(VideoID),
  Date DATE
);

CREATE TABLE RoomData (
  RoomID INT PRIMARY KEY,
  HostID INT,
  FOREIGN KEY (HostID) REFERENCES UserData(UserID),
  ParticipantIDs ARRAY,
  StartTime DATETIME,
  EndTime DATETIME
);

CREATE TABLE ChallengeData (
  ChallengeID INT PRIMARY KEY,
  ChallengeName VARCHAR(255),
  StartDate DATE,
  EndDate DATE
);

CREATE TABLE Reports (
  ReportID INT PRIMARY KEY,
  UserID INT,
  FOREIGN KEY (UserID) REFERENCES UserData(UserID),
  VideoID INT,
  FOREIGN KEY (VideoID) REFERENCES VideoData(VideoID),
  ReportReason VARCHAR(255),
  ReportDate DATE
);

CREATE TABLE Messages (
  MessageID INT PRIMARY KEY,
  SenderID INT,
  FOREIGN KEY (SenderID) REFERENCES UserData(UserID),
  ReceiverID INT,
  FOREIGN KEY (ReceiverID) REFERENCES UserData(UserID),
  Message VARCHAR(255),
  SendDate DATE,
  ReadDate DATE
);