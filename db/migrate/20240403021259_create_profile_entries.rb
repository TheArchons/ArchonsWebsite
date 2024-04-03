class CreateProfileEntries < ActiveRecord::Migration[7.1]
  def change
    create_table :profile_entries do |t|
      t.string :type
      t.string :value

      t.timestamps
    end
  end
end
