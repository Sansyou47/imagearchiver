drop table if exists users;
create table users(
    userId      int primary key auto_increment,
    userName    varchar(255) not null,
    email       varchar(255),
    password    varchar(255) not null
);

INSERT INTO users(userName, email, password) VALUES ('テストユーザー', 'test@localhost.jp', 'testuser');

drop table if exists images;
create table images(
    imageId     int primary key auto_increment,
    imageName   varchar(255) not null,
    filePath    varchar(255) not null,
    fileType    varchar(255) not null,
    fileSize    int not null,
    importDate  datetime default current_timestamp,
    userId      int not null
);