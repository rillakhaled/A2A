class CreateProfiles < ActiveRecord::Migration[6.1]
  def change
    create_table :profiles do |t|
      t.string :name

      t.timestamps
    end

    create_table :users do |t|
      t.integer :user_id
      t.timestamps
    end
  end
end
