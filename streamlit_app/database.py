import psycopg2
import pandas as pd
import streamlit as st
import os

@st.cache_resource
def get_db_connection():
    """Get RDS connection (returns None if unavailable)"""
    return None

def is_db_available():
    """Check if database is reachable"""
    return False

def get_patient_from_db(patient_id):
    """Fetch patient from RDS (returns None if DB unavailable)"""
    return None

def get_all_patients_from_db():
    """Get all patients from RDS (returns None if unavailable)"""
    return None