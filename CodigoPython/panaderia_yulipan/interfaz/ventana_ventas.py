"""
Ventana para el CRUD de ventas en la panadería YULIPAN MAGANGUE
"""
import tkinter as tk
from tkinter import ttk, messagebox

class VentanaVentas:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Ventas - Panadería YULIPAN MAGANGUE")
        self.master.geometry("700x400")

        # Frame de formulario
        frame_form = tk.Frame(master)
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Código:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_codigo = tk.Entry(frame_form)
        self.entry_codigo.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Producto:").grid(row=0, column=2, padx=5, pady=5)
        self.entry_producto = tk.Entry(frame_form)
        self.entry_producto.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_form, text="Cantidad:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_cantidad = tk.Entry(frame_form)
        self.entry_cantidad.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Precio:").grid(row=1, column=2, padx=5, pady=5)
        self.entry_precio = tk.Entry(frame_form)
        self.entry_precio.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(frame_form, text="Fecha (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5)
        self.entry_fecha = tk.Entry(frame_form)
        self.entry_fecha.grid(row=2, column=1, padx=5, pady=5)

        # Botones de acción
        frame_btns = tk.Frame(master)
        frame_btns.pack(pady=5)
        tk.Button(frame_btns, text="Agregar", command=self.agregar_venta).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btns, text="Modificar", command=self.modificar_venta).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btns, text="Eliminar", command=self.eliminar_venta).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btns, text="Limpiar", command=self.limpiar_formulario).pack(side=tk.LEFT, padx=5)

        # Tabla de ventas
        self.tabla = ttk.Treeview(master, columns=("codigo", "producto", "cantidad", "precio", "fecha", "total"), show="headings")
        self.tabla.heading("codigo", text="Código")
        self.tabla.heading("producto", text="Producto")
        self.tabla.heading("cantidad", text="Cantidad")
        self.tabla.heading("precio", text="Precio")
        self.tabla.heading("fecha", text="Fecha")
        self.tabla.heading("total", text="Total")
        self.tabla.pack(fill=tk.BOTH, expand=True, pady=10)
        self.tabla.bind("<ButtonRelease-1>", self.seleccionar_fila)

        # Datos de ejemplo
        self.ventas = []
        self.cargar_ventas()

    def agregar_venta(self):
        try:
            codigo = self.entry_codigo.get()
            producto = self.entry_producto.get()
            cantidad = int(self.entry_cantidad.get())
            precio = float(self.entry_precio.get())
            fecha = self.entry_fecha.get()
            total = cantidad * precio
            self.ventas.append({
                "codigo": codigo,
                "producto": producto,
                "cantidad": cantidad,
                "precio": precio,
                "fecha": fecha,
                "total": total
            })
            self.cargar_ventas()
            self.limpiar_formulario()
            messagebox.showinfo("Éxito", "Venta agregada correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")

    def modificar_venta(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una venta para modificar.")
            return
        idx = int(seleccion[0])
        try:
            self.ventas[idx]["codigo"] = self.entry_codigo.get()
            self.ventas[idx]["producto"] = self.entry_producto.get()
            self.ventas[idx]["cantidad"] = int(self.entry_cantidad.get())
            self.ventas[idx]["precio"] = float(self.entry_precio.get())
            self.ventas[idx]["fecha"] = self.entry_fecha.get()
            self.ventas[idx]["total"] = self.ventas[idx]["cantidad"] * self.ventas[idx]["precio"]
            self.cargar_ventas()
            self.limpiar_formulario()
            messagebox.showinfo("Éxito", "Venta modificada correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")

    def eliminar_venta(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una venta para eliminar.")
            return
        idx = int(seleccion[0])
        del self.ventas[idx]
        self.cargar_ventas()
        self.limpiar_formulario()
        messagebox.showinfo("Éxito", "Venta eliminada correctamente.")

    def limpiar_formulario(self):
        self.entry_codigo.delete(0, tk.END)
        self.entry_producto.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
        self.entry_fecha.delete(0, tk.END)

    def cargar_ventas(self):
        for i in self.tabla.get_children():
            self.tabla.delete(i)
        for idx, venta in enumerate(self.ventas):
            self.tabla.insert("", "end", iid=idx, values=(
                venta["codigo"], venta["producto"], venta["cantidad"], venta["precio"], venta["fecha"], venta["total"]
            ))

    def seleccionar_fila(self, event):
        seleccion = self.tabla.selection()
        if not seleccion:
            return
        idx = int(seleccion[0])
        venta = self.ventas[idx]
        self.entry_codigo.delete(0, tk.END)
        self.entry_codigo.insert(0, venta["codigo"])
        self.entry_producto.delete(0, tk.END)
        self.entry_producto.insert(0, venta["producto"])
        self.entry_cantidad.delete(0, tk.END)
        self.entry_cantidad.insert(0, venta["cantidad"])
        self.entry_precio.delete(0, tk.END)
        self.entry_precio.insert(0, venta["precio"])
        self.entry_fecha.delete(0, tk.END)
        self.entry_fecha.insert(0, venta["fecha"])
