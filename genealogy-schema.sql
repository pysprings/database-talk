CREATE TABLE family (
    id integer primary key autoincrement not null,
    name TEXT NOT NULL,
    father INTEGER,
    mother INTEGER,
    FOREIGN KEY(father) REFERENCES family(oid),
    FOREIGN KEY(mother) REFERENCES family(oid)
);
