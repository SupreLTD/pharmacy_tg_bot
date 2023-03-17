create table basket
(
    id         int auto_increment
        primary key,
    user_id    text not null,
    product_id int  not null
);

create table pharmacy
(
    id      int auto_increment
        primary key,
    name    text not null,
    address text not null
);

create table product
(
    id           int auto_increment
        primary key,
    name         text  not null,
    price        float not null,
    pharmacy_id  int   not null,
    manufacturer text  not null,
    expires      date  null
);

