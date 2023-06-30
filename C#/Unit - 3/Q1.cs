using System;
using System.Windows.Forms;

namespace MyApplication
{
    public class MyForm : Form
    {
        // Add your controls and other members here

        public MyForm()
        {
            // Initialize the form
            InitializeComponents();
        }

        private void InitializeComponents()
        {
            // Set form properties
            this.Text = "My Application";
            this.Size = new System.Drawing.Size(400, 300);

            // Create controls
            Button myButton = new Button();
            myButton.Text = "Click Me!";
            myButton.Location = new System.Drawing.Point(100, 100);
            myButton.Click += MyButton_Click;

            // Add controls to the form
            this.Controls.Add(myButton);
        }

        private void MyButton_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Button clicked!");
        }
    }

    public static class Program
    {
        [STAThread]
        public static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);

            // Create and run the main form
            Application.Run(new MyForm());
        }
    }
}
