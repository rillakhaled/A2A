class ChangeTableProfilesAgeGenderLocation < ActiveRecord::Migration[6.1]
  def change
    add_column :profiles, :age, :int
    add_column :profiles, :gender, :string
    add_column :profiles, :location, :string
  end
end
