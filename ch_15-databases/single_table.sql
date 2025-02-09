CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Kamron', 34);
INSERT INTO Ages (name, age) VALUES ('Brigitte', 39);
INSERT INTO Ages (name, age) VALUES ('Ryder', 30);
INSERT INTO Ages (name, age) VALUES ('Alexi', 15);

SELECT hex(name || age) AS X FROM Ages ORDER BY X