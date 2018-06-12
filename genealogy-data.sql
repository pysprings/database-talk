INSERT INTO family (name) VALUES
    ("Terah"),
    ("Amathlai"),
    ("Sarah"),
    ("Hagar"),
    ("Rebecca");

INSERT INTO family (name, father, mother)  VALUES
    ("Abraham", (select id from family where name = "Terah"), (select id from family where name = "Amathlai")),
    ("Isaac", (select id from family where name = "Abraham"), (select id from family where name = "Sarah")),
    ("Ishmael", (select id from family where name = "Abraham"), (select id from family where name = "Hagar")),
    ("Jacob", (select id from family where name = "Isaac"), (select id from family where name = "Rebecca"));
