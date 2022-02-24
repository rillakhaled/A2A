class AddColumnsToProfile < ActiveRecord::Migration[6.1]
  def change
    add_column :profiles, :cultureScore, :integer
    add_column :profiles, :facialScore, :integer
    add_column :profiles, :lifestyleScore, :integer
    add_column :profiles, :kundaliScore, :integer
    add_column :profiles, :locationScore, :integer
  end
end
