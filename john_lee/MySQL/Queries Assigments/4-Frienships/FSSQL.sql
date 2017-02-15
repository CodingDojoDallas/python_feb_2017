-- INSERT INTO users (id, users.first_name, users.last_name, created_at, updated_at)
-- VALUES(,"", "", NOW(), NOW());

-- DELETE FROM users where id = ;

-- SELECT * FROM users 

-- insert into friendships (user_id, friend_id) VALUES(,);

SELECT users.first_name, users.last_name, user2.first_name as friend_first_name, user2.last_name as friend_last_name from users
LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as user2 ON friendships.friend_id = user2.id;
