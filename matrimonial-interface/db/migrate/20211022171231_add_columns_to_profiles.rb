class AddColumnsToProfiles < ActiveRecord::Migration[6.1]
  def change
    add_column :profiles, :job, :string
    add_column :profiles, :salary, :integer
    add_column :profiles, :religion, :string
    add_column :profiles, :about, :string
    add_column :profiles, :interests, :string
  end
end
