/*
=====================
1. ADMIN (base admin)
=====================
*/
db = db.getSiblingDB("admin");

db.createUser({
  user: "admin_user",
  pwd: "admin_password",
  roles: [
    { role: "root", db: "admin" }
  ]
});

/*
=====================
2. APPLICATION / MIGRATION
=====================
*/
db = db.getSiblingDB("medicaldb");

db.createUser({
  user: "app_user",
  pwd: "app_password",
  roles: [
    { role: "readWrite", db: "medicaldb" }
  ]
});

/*
=====================
3. READ ONLY
=====================
*/
db.createUser({
  user: "readonly_user",
  pwd: "readonly_password",
  roles: [
    { role: "read", db: "medicaldb" }
  ]
});
