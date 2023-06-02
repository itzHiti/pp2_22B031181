CREATE TABLE phonebookk (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL UNIQUE
);

CREATE OR REPLACE FUNCTION search_users(pattern VARCHAR)
RETURNS SETOF users AS $$
BEGIN
    RETURN QUERY SELECT * FROM users WHERE name LIKE '%' || pattern || '%'
        OR surname LIKE '%' || pattern || '%'
        OR phone LIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;


SELECT * FROM search_users('tochno');


CREATE OR REPLACE PROCEDURE upsert_user(name VARCHAR, phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO users (name, phone)
    VALUES (name, phone)
    ON CONFLICT (name)
    DO UPDATE SET phone = EXCLUDED.phone;
END;
$$;


CALL upsert_user('tochno useful', '87776661234');
CALL upsert_user('tochno real', '88002281337');


CREATE OR REPLACE PROCEDURE insert_users(users user[])
LANGUAGE plpgsql
AS $$
DECLARE
    invalid_users user[];
BEGIN
    invalid_users := ARRAY[]::user[];
    FOREACH u IN ARRAY users
    LOOP
        IF NOT (u.phone ~ E'^\\d{10}$') THEN
            invalid_users := array_append(invalid_users, u);
        ELSE
            INSERT INTO users (name, phone)
            VALUES (u.name, u.phone);
        END IF;
    END LOOP;
    RETURN invalid_users;
END;
$$;


CALL insert_users(ARRAY[
    ('User Name', '87895461234'),
    ('Name Surname', '87779651234'),
    ('Fake User', '89991337556')
]::user[]);


CREATE OR REPLACE FUNCTION get_users(limit INTEGER, offset INTEGER)
RETURNS SETOF users AS $$
BEGIN
    RETURN QUERY SELECT * FROM users ORDER BY id LIMIT limit OFFSET offset;
END;
$$ LANGUAGE plpgsql;


SELECT * FROM get_users(10, 20);



CREATE OR REPLACE PROCEDURE delete_user_by_name_or_phone(name_or_phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM users WHERE name = name_or_phone OR phone = name_or_phone;
END;
$$;

CALL delete_user_by_name_or_phone('Fake User');

