SELECT u.first_name, u.last_name, f.first_name AS friend_fn, f.last_name AS friend_ln FROM users u
LEFT JOIN friendships  ON u.id = friendships.users_id
LEFT JOIN users as f ON f.id = friendships.friend_id;
