from flask import Blueprint, render_template, session
dashboard_bp=Blueprint("dashboard",__name__)
@dashboard_bp.route("/dashboard")
def dashboard():
    if session.get("login_type")=="superadmin":
        return render_template("dashboard/superadmin_dashboard.html")
    return render_template("dashboard/client_dashboard.html")
