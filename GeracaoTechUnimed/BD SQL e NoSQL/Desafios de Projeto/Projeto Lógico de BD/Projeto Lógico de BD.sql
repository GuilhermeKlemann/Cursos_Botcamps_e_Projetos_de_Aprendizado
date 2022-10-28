create database osoficina;
use osoficina;

create table clients(
		idClient int auto_increment primary key,
        Fname varchar(15),
        Minit char(3),
        Lname varchar(25),
        CPF char(11) not null,
        Address varchar(255),
        Phonenumber varchar(15),
        constraint unique_cpf_client unique (CPF)
);

alter table clients auto_increment=1;

create table vehicle(
		idVehicle int primary key,
        licensePlate varchar(9) not null,
        model varchar(30) not null,
        vehicleYear year(4) not null
);

create table mechanic (
		idMechanic int primary key,
        Fullname varchar(50),
        Address varchar(255),
        Phonenumber varchar(15),
        mechanicID varchar(9)
);

create table basicInfos(
	idBasicInfos int primary key,
	constraint fk_basic_Infos foreign key (idClient) references clients(idClient),
    constraint fk_basic_Infos foreign key (idVehicle) references vehicle(idVehicle)
);

create table triageTeam(
	idTriageTeam int primary key,
	constraint fk_triage_Team foreign key (idMechanic) references mechanic(idMechanic),
    constraint fk_triage_Team foreign key (idBasicInfos) references basicInfos(idBasicInfos)
);

create table products(
	idProducts int primary key,
    productName varchar(45),
    productCode varchar(12),
    productPrice double
);

create table labor(
	idLabor int primary key,
    serviceType varchar(45),
    serviceCode varchar(12),
    servicePrice double
);

create table budgetAndEvaluation(
	idBudgetAndEvaluation int primary key,
    serviceDescription varchar(90),
	constraint fk_budget_And_Evaluation foreign key (idTriageTeam) references triageTeam(idTriageTeam),
    constraint fk_budget_And_Evaluation foreign key (idProducts) references products(idProducts),
    constraint fk_budget_And_Evaluation foreign key (idLabor) references labor(idLabor)
);

create table os(
	idOS int primary key,
    osStatus enum('Pendente', 'Avaliação', 'Aguardando Pagamento', 'Aprovação', 'Pronto', 'Finalizado'),
    issueDate datetime,
    conclusionDate datetime,
    osNumber varchar(12),
    amount double,
    authorization tinyint,
    constraint fk_os foreign key (idBudgetAndEvaluation) references budgetAndEvaluation(idBudgetAndEvaluation)
);



show tables;

show databases;
use information_schema;
show tables;
desc referential_constraints;
select * from referential_constraints where constraint_schema = 'osoficina';