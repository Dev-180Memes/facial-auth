package database

import (
	"github.com/Dev-180Memes/facial-auth/models"
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

var DB *gorm.DB

func Connect() {
	connection, err := gorm.Open(mysql.Open("devuser:password@/user_db"), &gorm.Config{})
	if err != nil {
		panic("Could not connect to the database")
	}
	DB = connection

	// Migrate the schema
	err = connection.AutoMigrate(&models.User{})
	if err != nil {
		return
	}
}
