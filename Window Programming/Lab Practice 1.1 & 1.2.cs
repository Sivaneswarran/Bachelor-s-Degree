using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btn_add_Click(object sender, EventArgs e)
        {
            //Input
            int num1 = int.Parse(txt_num1.Text);
            int num2 = int.Parse(txt_num2.Text);
            
            //Output
            lbl_sum.Text = (num1 + num2).ToString();
        }

        private void btn_clear_Click(object sender, EventArgs e)
        {
            txt_num1.Text = "";
            txt_num2.Text = "";
            lbl_sum.Text = "";
        }
    }
}
