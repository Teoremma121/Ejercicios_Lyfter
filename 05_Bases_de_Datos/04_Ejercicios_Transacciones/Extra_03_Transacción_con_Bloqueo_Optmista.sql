SET search_path TO "Ejercicios_Transactions";

DO $$
DECLARE
    -- Definimos variables para almacenar datos durante la ejecución
    v_product_id INTEGER := 3;
	v_quantity INTEGER := 1;
	v_price REAL;
	v_available_stock INTEGER;
	v_buyer VARCHAR(50) := 'hello_kitty_bows';
	v_user_id INTEGER;
	v_bill_id INTEGER;
	v_total_amount REAL;
	v_invoice_number VARCHAR(15) := 'INV-202607-1009';

BEGIN
    -- 1. Verificación preliminar de las existencias
    SELECT stock INTO v_available_stock
    FROM products
    WHERE id = v_product_id;

    IF v_available_stock IS NULL OR v_available_stock < v_quantity THEN
      RAISE EXCEPTION 'No hay suficientes unidades del producto en el inventario';
    END IF;

	SELECT price INTO v_price
    FROM products
    WHERE id = v_product_id;

	-- 2. Insertar la factura
	SELECT id INTO v_user_id
	FROM users
	WHERE username = v_buyer;

	IF v_user_id IS NULL THEN
	  RAISE EXCEPTION 'El usuario no existe en la base de datos';
	END IF;

    INSERT INTO bills (invoice_number, user_id)
    VALUES (v_invoice_number, v_user_id);

	SELECT id INTO v_bill_id
	FROM bills
	WHERE invoice_number = v_invoice_number;

	-- 3. Insertar el detalle
	INSERT INTO "bill-product" (bill_id, product_id, quantity, amount)
	VALUES 
	(v_bill_id, v_product_id, v_quantity, v_price*v_quantity);

	SELECT SUM(amount) INTO v_total_amount
	FROM "bill-product"
	WHERE bill_id = v_bill_id
	GROUP BY bill_id;
	
	-- 4. Terminar la factura
	UPDATE bills
	SET total_amount = v_total_amount
	WHERE id = v_bill_id;

    -- 5. Comprobación definitiva del stock
    SELECT stock INTO v_available_stock
    FROM products
    WHERE id = v_product_id;

    IF v_available_stock < v_quantity THEN
      RAISE EXCEPTION 'El producto está agotado';
    END IF;
	
    -- 6. Reducir el stock del producto
    UPDATE products
    SET stock = stock - v_quantity
    WHERE id = v_product_id;

	RAISE NOTICE 'Compra finalizada.';
END $$;