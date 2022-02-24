class RemoveUserIdFromProfiles < ActiveRecord::Migration[6.1]
  def change
    remove_column :profiles, :userID
  end
end
