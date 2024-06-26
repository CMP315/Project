﻿namespace SecureSoftware.Forms
{
    partial class Register
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            CancelButton = new Button();
            NameInputBox = new TextBox();
            RegisterButton = new Button();
            label1 = new Label();
            tableLayoutPanel1 = new TableLayoutPanel();
            tableLayoutPanel2 = new TableLayoutPanel();
            label4 = new Label();
            label5 = new Label();
            iconPictureBox2 = new FontAwesome.Sharp.IconPictureBox();
            label3 = new Label();
            iconPictureBox1 = new FontAwesome.Sharp.IconPictureBox();
            tableLayoutPanel3 = new TableLayoutPanel();
            label2 = new Label();
            PasswordBox = new TextBox();
            EMailInputBox = new TextBox();
            label6 = new Label();
            iconPictureBox3 = new FontAwesome.Sharp.IconPictureBox();
            PasswordInputBox = new TextBox();
            ShowPasswordCheckBox = new CheckBox();
            tableLayoutPanel1.SuspendLayout();
            tableLayoutPanel2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)iconPictureBox2).BeginInit();
            ((System.ComponentModel.ISupportInitialize)iconPictureBox1).BeginInit();
            tableLayoutPanel3.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)iconPictureBox3).BeginInit();
            SuspendLayout();
            // 
            // CancelButton
            // 
            CancelButton.BackColor = Color.FromArgb(192, 57, 43);
            CancelButton.Cursor = Cursors.Hand;
            CancelButton.Dock = DockStyle.Fill;
            CancelButton.FlatAppearance.BorderSize = 0;
            CancelButton.FlatAppearance.MouseDownBackColor = Color.FromArgb(192, 57, 43);
            CancelButton.FlatAppearance.MouseOverBackColor = Color.FromArgb(231, 76, 60);
            CancelButton.FlatStyle = FlatStyle.Flat;
            CancelButton.Font = new Font("Tahoma", 15.75F, FontStyle.Bold, GraphicsUnit.Point);
            CancelButton.ForeColor = Color.White;
            CancelButton.Location = new Point(183, 0);
            CancelButton.Margin = new Padding(0);
            CancelButton.Name = "CancelButton";
            CancelButton.Size = new Size(184, 60);
            CancelButton.TabIndex = 4;
            CancelButton.Text = "CANCEL";
            CancelButton.UseVisualStyleBackColor = false;
            CancelButton.Click += CancelButton_Click;
            // 
            // NameInputBox
            // 
            NameInputBox.Location = new Point(48, 114);
            NameInputBox.Name = "NameInputBox";
            NameInputBox.Size = new Size(311, 23);
            NameInputBox.TabIndex = 0;
            NameInputBox.Text = "Test User";
            // 
            // RegisterButton
            // 
            RegisterButton.BackColor = Color.FromArgb(39, 174, 96);
            RegisterButton.Cursor = Cursors.Hand;
            RegisterButton.Dock = DockStyle.Fill;
            RegisterButton.FlatAppearance.BorderSize = 0;
            RegisterButton.FlatAppearance.MouseDownBackColor = Color.FromArgb(39, 174, 96);
            RegisterButton.FlatAppearance.MouseOverBackColor = Color.FromArgb(46, 204, 113);
            RegisterButton.FlatStyle = FlatStyle.Flat;
            RegisterButton.Font = new Font("Tahoma", 15.75F, FontStyle.Bold, GraphicsUnit.Point);
            RegisterButton.ForeColor = Color.White;
            RegisterButton.Location = new Point(0, 0);
            RegisterButton.Margin = new Padding(0);
            RegisterButton.Name = "RegisterButton";
            RegisterButton.Size = new Size(183, 60);
            RegisterButton.TabIndex = 3;
            RegisterButton.Text = "REGISTER";
            RegisterButton.UseVisualStyleBackColor = false;
            RegisterButton.Click += RegisterButton_ClickAsync;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point);
            label1.ForeColor = Color.Black;
            label1.Location = new Point(48, 90);
            label1.Margin = new Padding(0);
            label1.Name = "label1";
            label1.Size = new Size(52, 21);
            label1.TabIndex = 4;
            label1.Text = "Name";
            // 
            // tableLayoutPanel1
            // 
            tableLayoutPanel1.ColumnCount = 2;
            tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 50F));
            tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 50F));
            tableLayoutPanel1.Controls.Add(RegisterButton, 0, 0);
            tableLayoutPanel1.Controls.Add(CancelButton, 1, 0);
            tableLayoutPanel1.Dock = DockStyle.Bottom;
            tableLayoutPanel1.Location = new Point(0, 289);
            tableLayoutPanel1.Margin = new Padding(0);
            tableLayoutPanel1.Name = "tableLayoutPanel1";
            tableLayoutPanel1.RowCount = 1;
            tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 100F));
            tableLayoutPanel1.Size = new Size(367, 60);
            tableLayoutPanel1.TabIndex = 6;
            // 
            // tableLayoutPanel2
            // 
            tableLayoutPanel2.BackColor = Color.FromArgb(142, 68, 173);
            tableLayoutPanel2.ColumnCount = 1;
            tableLayoutPanel2.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 100F));
            tableLayoutPanel2.Controls.Add(label4, 0, 0);
            tableLayoutPanel2.Controls.Add(label5, 0, 1);
            tableLayoutPanel2.Dock = DockStyle.Top;
            tableLayoutPanel2.Location = new Point(0, 0);
            tableLayoutPanel2.Name = "tableLayoutPanel2";
            tableLayoutPanel2.RowCount = 2;
            tableLayoutPanel2.RowStyles.Add(new RowStyle(SizeType.Absolute, 50F));
            tableLayoutPanel2.RowStyles.Add(new RowStyle(SizeType.Absolute, 20F));
            tableLayoutPanel2.Size = new Size(367, 77);
            tableLayoutPanel2.TabIndex = 7;
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.BackColor = Color.FromArgb(100, 48, 122);
            label4.Dock = DockStyle.Fill;
            label4.Font = new Font("Showcard Gothic", 27.75F, FontStyle.Regular, GraphicsUnit.Point);
            label4.ForeColor = Color.White;
            label4.Location = new Point(0, 0);
            label4.Margin = new Padding(0);
            label4.Name = "label4";
            label4.Size = new Size(367, 50);
            label4.TabIndex = 0;
            label4.Text = "PASSMAN";
            label4.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Dock = DockStyle.Fill;
            label5.Font = new Font("Segoe UI", 12F, FontStyle.Italic, GraphicsUnit.Point);
            label5.ForeColor = Color.White;
            label5.Location = new Point(3, 50);
            label5.Name = "label5";
            label5.Size = new Size(361, 27);
            label5.TabIndex = 1;
            label5.Text = "\"A simple and secure Password Manager!\"";
            label5.TextAlign = ContentAlignment.TopCenter;
            // 
            // iconPictureBox2
            // 
            iconPictureBox2.BackColor = Color.Transparent;
            iconPictureBox2.ForeColor = Color.Black;
            iconPictureBox2.IconChar = FontAwesome.Sharp.IconChar.User;
            iconPictureBox2.IconColor = Color.Black;
            iconPictureBox2.IconFont = FontAwesome.Sharp.IconFont.Auto;
            iconPictureBox2.IconSize = 31;
            iconPictureBox2.Location = new Point(9, 85);
            iconPictureBox2.Margin = new Padding(0);
            iconPictureBox2.Name = "iconPictureBox2";
            iconPictureBox2.Size = new Size(39, 31);
            iconPictureBox2.TabIndex = 5;
            iconPictureBox2.TabStop = false;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point);
            label3.ForeColor = Color.Black;
            label3.Location = new Point(48, 149);
            label3.Margin = new Padding(0);
            label3.Name = "label3";
            label3.Size = new Size(54, 21);
            label3.TabIndex = 5;
            label3.Text = "E-Mail";
            // 
            // iconPictureBox1
            // 
            iconPictureBox1.BackColor = Color.Transparent;
            iconPictureBox1.ForeColor = Color.Black;
            iconPictureBox1.IconChar = FontAwesome.Sharp.IconChar.Envelope;
            iconPictureBox1.IconColor = Color.Black;
            iconPictureBox1.IconFont = FontAwesome.Sharp.IconFont.Auto;
            iconPictureBox1.IconSize = 31;
            iconPictureBox1.Location = new Point(9, 145);
            iconPictureBox1.Margin = new Padding(0);
            iconPictureBox1.Name = "iconPictureBox1";
            iconPictureBox1.Size = new Size(39, 31);
            iconPictureBox1.TabIndex = 6;
            iconPictureBox1.TabStop = false;
            // 
            // tableLayoutPanel3
            // 
            tableLayoutPanel3.ColumnCount = 2;
            tableLayoutPanel3.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 9.420289F));
            tableLayoutPanel3.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 90.57971F));
            tableLayoutPanel3.Controls.Add(label2, 1, 0);
            tableLayoutPanel3.Location = new Point(0, 0);
            tableLayoutPanel3.Name = "tableLayoutPanel3";
            tableLayoutPanel3.RowCount = 1;
            tableLayoutPanel3.RowStyles.Add(new RowStyle(SizeType.Absolute, 20F));
            tableLayoutPanel3.Size = new Size(200, 100);
            tableLayoutPanel3.TabIndex = 0;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point);
            label2.Location = new Point(18, 0);
            label2.Margin = new Padding(0);
            label2.Name = "label2";
            label2.Size = new Size(76, 21);
            label2.TabIndex = 5;
            label2.Text = "Password";
            // 
            // PasswordBox
            // 
            PasswordBox.Dock = DockStyle.Fill;
            PasswordBox.Location = new Point(21, 24);
            PasswordBox.Name = "PasswordBox";
            PasswordBox.PasswordChar = '●';
            PasswordBox.Size = new Size(176, 23);
            PasswordBox.TabIndex = 2;
            // 
            // EMailInputBox
            // 
            EMailInputBox.Location = new Point(48, 173);
            EMailInputBox.Name = "EMailInputBox";
            EMailInputBox.Size = new Size(311, 23);
            EMailInputBox.TabIndex = 1;
            EMailInputBox.Text = "abc@test.com";
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point);
            label6.ForeColor = Color.Black;
            label6.Location = new Point(48, 212);
            label6.Margin = new Padding(0);
            label6.Name = "label6";
            label6.Size = new Size(76, 21);
            label6.TabIndex = 9;
            label6.Text = "Password";
            // 
            // iconPictureBox3
            // 
            iconPictureBox3.BackColor = Color.Transparent;
            iconPictureBox3.ForeColor = Color.Black;
            iconPictureBox3.IconChar = FontAwesome.Sharp.IconChar.Lock;
            iconPictureBox3.IconColor = Color.Black;
            iconPictureBox3.IconFont = FontAwesome.Sharp.IconFont.Auto;
            iconPictureBox3.IconSize = 31;
            iconPictureBox3.Location = new Point(9, 208);
            iconPictureBox3.Margin = new Padding(0);
            iconPictureBox3.Name = "iconPictureBox3";
            iconPictureBox3.Size = new Size(39, 31);
            iconPictureBox3.TabIndex = 10;
            iconPictureBox3.TabStop = false;
            // 
            // PasswordInputBox
            // 
            PasswordInputBox.Location = new Point(48, 236);
            PasswordInputBox.Name = "PasswordInputBox";
            PasswordInputBox.Size = new Size(311, 23);
            PasswordInputBox.TabIndex = 2;
            PasswordInputBox.Text = "testpass";
            PasswordInputBox.UseSystemPasswordChar = true;
            // 
            // ShowPasswordCheckBox
            // 
            ShowPasswordCheckBox.AutoSize = true;
            ShowPasswordCheckBox.Location = new Point(48, 261);
            ShowPasswordCheckBox.Name = "ShowPasswordCheckBox";
            ShowPasswordCheckBox.Size = new Size(108, 19);
            ShowPasswordCheckBox.TabIndex = 11;
            ShowPasswordCheckBox.Text = "Show Password";
            ShowPasswordCheckBox.UseVisualStyleBackColor = true;
            ShowPasswordCheckBox.CheckedChanged += ShowPasswordCheckBox_CheckedChanged;
            // 
            // Register
            // 
            AcceptButton = RegisterButton;
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = SystemColors.Control;
            ClientSize = new Size(367, 349);
            Controls.Add(ShowPasswordCheckBox);
            Controls.Add(label6);
            Controls.Add(iconPictureBox3);
            Controls.Add(PasswordInputBox);
            Controls.Add(label3);
            Controls.Add(iconPictureBox2);
            Controls.Add(iconPictureBox1);
            Controls.Add(NameInputBox);
            Controls.Add(label1);
            Controls.Add(EMailInputBox);
            Controls.Add(tableLayoutPanel2);
            Controls.Add(tableLayoutPanel1);
            MaximizeBox = false;
            MinimizeBox = false;
            Name = "Register";
            StartPosition = FormStartPosition.CenterScreen;
            Text = "Login";
            tableLayoutPanel1.ResumeLayout(false);
            tableLayoutPanel2.ResumeLayout(false);
            tableLayoutPanel2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)iconPictureBox2).EndInit();
            ((System.ComponentModel.ISupportInitialize)iconPictureBox1).EndInit();
            tableLayoutPanel3.ResumeLayout(false);
            tableLayoutPanel3.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)iconPictureBox3).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private new Button CancelButton;
        private TextBox NameInputBox;
        private Button RegisterButton;
        private Label label1;
        private TableLayoutPanel tableLayoutPanel1;
        private TableLayoutPanel tableLayoutPanel2;
        private FontAwesome.Sharp.IconPictureBox iconPictureBox2;
        private Label label3;
        private FontAwesome.Sharp.IconPictureBox iconPictureBox1;
        private TableLayoutPanel tableLayoutPanel3;
        private Label label2;
        private TextBox PasswordBox;
        private Label label4;
        private Label label5;
        private TextBox EMailInputBox;
        private Label label6;
        private FontAwesome.Sharp.IconPictureBox iconPictureBox3;
        private TextBox PasswordInputBox;
        private CheckBox ShowPasswordCheckBox;
    }
}