using System;
using System.Windows.Forms;

namespace MDIApplication
{
    public partial class MainForm : Form
    {
        private int childFormCounter = 0;

        public MainForm()
        {
            InitializeComponent();
        }

        private void MainForm_Load(object sender, EventArgs e)
        {
            // Set the IsMdiContainer property of the main form to true
            IsMdiContainer = true;
        }

        private void openChildFormToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // Create a new child form
            ChildForm childForm = new ChildForm();
            childForm.MdiParent = this; // Set the MdiParent property of the child form to the main form
            childForm.Text = "Child Form " + (++childFormCounter).ToString();
            childForm.Show();
        }

        private void openDialogToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // Create and display a dialog box
            DialogForm dialogForm = new DialogForm();
            dialogForm.ShowDialog();
        }
    }

    public partial class ChildForm : Form
    {
        public ChildForm()
        {
            InitializeComponent();
        }
    }

    public partial class DialogForm : Form
    {
        public DialogForm()
        {
            InitializeComponent();
        }

        private void DialogForm_Load(object sender, EventArgs e)
        {
            // Code for dialog form initialization
        }
    }

    static class Program
    {
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new MainForm());
        }
    }
}
