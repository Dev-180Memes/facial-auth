package models

type User struct {
	Id        uint   `json:"id" gorm:"column:id"`
	FirstName string `json:"first_name" gorm:"column:firstname"`
	LastName  string `json:"last_name" gorm:"column:lastname"`
	Email     string `json:"email" gorm:"column:email;unique"`
	Password  []byte `json:"-" gorm:"column:password"`
	FaceId    string `json:"face_id" gorm:"column:face_id"`
}
