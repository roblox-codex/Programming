using System;
using System.Data;
using System.Data.SqlClient;
using System.Windows.Forms;

namespace ADO.NET_Bound_Mode
{
    public partial class MainForm : Form
    {
        private string connectionString = "Your_Connection_String";
        private SqlConnection connection;
        private SqlDataAdapter dataAdapter;
        private DataTable dataTable;

        public MainForm()
        {
            InitializeComponent();
        }

        private void MainForm_Load(object sender, EventArgs e)
        {
            connection = new SqlConnection(connectionString);
            dataTable = new DataTable();
            dataAdapter = new SqlDataAdapter("SELECT * FROM Your_Table", connection);

            // Fill the DataTable with data from the database
            dataAdapter.Fill(dataTable);

            // Set the DataTable as the data source for the DataGridView
            dataGridView.DataSource = dataTable;
        }

        private void btnAdd_Click(object sender, EventArgs e)
        {
            // Add a new row to the DataTable
            DataRow newRow = dataTable.NewRow();
            dataTable.Rows.Add(newRow);
        }

        private void btnSave_Click(object sender, EventArgs e)
        {
            // Save the changes back to the database
            dataAdapter.Update(dataTable);
        }

        private void btnDelete_Click(object sender, EventArgs e)
        {
            // Delete the selected row from the DataTable
            if (dataGridView.SelectedRows.Count > 0)
            {
                dataGridView.Rows.Remove(dataGridView.SelectedRows[0]);
            }
        }

        private void btnSearch_Click(object sender, EventArgs e)
        {
            // Perform a search on the DataTable
            string searchText = txtSearch.Text;

            // Use the DataTable's Select method to filter rows
            DataRow[] rows = dataTable.Select("ColumnName = '" + searchText + "'");

            if (rows.Length > 0)
            {
                // Select the first matching row in the DataGridView
                int rowIndex = dataTable.Rows.IndexOf(rows[0]);
                dataGridView.Rows[rowIndex].Selected = true;
                dataGridView.FirstDisplayedScrollingRowIndex = rowIndex;
            }
            else
            {
                MessageBox.Show("No matching records found.");
            }
        }
    }
}
