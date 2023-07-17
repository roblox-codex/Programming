using System;
using System.Windows.Forms;

namespace MDIApplication
{
    public partial class Form1 : Form
    {
        private int childFormCounter = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            IsMdiContainer = true; // Set the IsMdiContainer property of the main form to true
        }

        private void openChildFormToolStripMenuItem_Click(object sender, EventArgs e)
        {
            ChildForm childForm = new ChildForm();
            childForm.MdiParent = this; // Set the MdiParent property of the child form to the main form
            childForm.Text = "Child Form " + (++childFormCounter).ToString();
            childForm.Show();
        }

        private void openDialogToolStripMenuItem_Click(object sender, EventArgs e)
        {
            DialogForm dialogForm = new DialogForm();
            dialogForm.ShowDialog();
        }
    }
}
