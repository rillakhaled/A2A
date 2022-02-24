class Profile < ApplicationRecord
    # validates :name, :age, :gender, :location, presence: true
    belongs_to :user, class_name: "User", foreign_key: "user_id"
end
