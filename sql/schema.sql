create table news_stock_data(
    id int auto_increment primary key,
    date date,
    title text,
    sentiment float,
    open_price float,
    close_price float,
    volume bigint
);

