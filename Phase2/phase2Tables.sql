CREATE TABLE DomainName
(
domain_id BIGSERIAL PRIMARY KEY,
domain_name char(30) NOT NULL
);

CREATE TABLE Address
(
address_id BIGSERIAL PRIMARY KEY,
address_name char(100) NOT NULL,
domain_id int references DomainName(domain_id)
);