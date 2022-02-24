class AddUserIdToProfiles < ActiveRecord::Migration[6.1]
  def change
    add_column :profiles, :user_id, :int
  end
end
