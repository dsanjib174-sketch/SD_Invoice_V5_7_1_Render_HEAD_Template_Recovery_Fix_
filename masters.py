from flask import Blueprint, render_template
masters_bp=Blueprint("masters",__name__)
@masters_bp.route("/masters")
def masters(): return render_template("masters/masters.html")
@masters_bp.route("/rate-contract")
def rate_contract(): return render_template("masters/rate_contract.html")
