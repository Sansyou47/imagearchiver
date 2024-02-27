drop table if exists users;
create table users(
    userId int primary key auto_increment,
    userName varchar(255) not null,
    email varchar(255),
    password varchar(255) not null
);

INSERT INTO users(userName, email, password) VALUES ('テストユーザー', 'test@localhost.jp', 'testuser');

drop table if exists files;
create table files(
    fileId int primary key auto_increment,
    fileName varchar(255) not null,
    filePath varchar(255) not null,
    userId int not null,
);