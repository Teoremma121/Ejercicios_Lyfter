SET search_path TO "Ejercicios_Transactions";

DO $$
DECLARE
    -- Definimos variables para almacenar datos durante la ejecución
    v_product_01_id INTEGER := 3;
	v_product_02_id INTEGER := 4;
	v_product_03_id INTEGER := 10;
	v_product_01_quantity INTEGER := 1;
	v_product_02_quantity INTEGER := 2;
	v_product_03_quantity INTEGER := 3;
	v_product_01_price REAL;
	v_product_02_price REAL;
	v_product_03_price REAL;
	v_available_stock INTEGER;
	v_buyer VARCHAR(50) := 'kuromi_goth_vibes';
	v_user_id INTEGER;
	v_bill_id INTEGER;
	v_total_amount REAL;
	v_invoice_number VARCHAR(15) := 'INV-202607-1007';

BEGIN
	-- 1. Crear la factura:
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
	
    -- 2. Verificación de existencias:
	-- 2.1 Primer Producto:
    SELECT stock INTO v_available_stock
    FROM products
    WHERE id = v_product_01_id;

    IF v_available_stock IS NULL OR v_available_stock < v_product_01_quantity THEN
      RAISE EXCEPTION 'No hay suficientes unidades del producto en el inventario';
    END IF;

	SELECT price INTO v_product_01_price
    FROM products
    WHERE id = v_product_01_id;

	-- 2.2 Segundo Producto:
    SELECT stock INTO v_available_stock
    FROM products
    WHERE id = v_product_02_id;

    IF v_available_stock IS NULL OR v_available_stock < v_product_02_quantity THEN
      RAISE EXCEPTION 'No hay suficientes unidades del producto en el inventario';
    END IF;

	SELECT price INTO v_product_02_price
    FROM products
    WHERE id = v_product_02_id;

	-- 2.3 Tercer Producto:
	SELECT stock INTO v_available_stock
    FROM products
    WHERE id = v_product_03_id;

    IF v_available_stock IS NULL OR v_available_stock < v_product_03_quantity THEN
      RAISE EXCEPTION 'No hay suficientes unidades del producto en el inventario';
    END IF;

	SELECT price INTO v_product_03_price
    FROM products
    WHERE id = v_product_03_id;

	-- 3. Insertar los detalles:
	INSERT INTO "bill-product" (bill_id, product_id, quantity, amount)
	VALUES 
	(v_bill_id, v_product_01_id, v_product_01_quantity, v_product_01_price*v_product_01_quantity),
	(v_bill_id, v_product_02_id, v_product_02_quantity, v_product_02_price*v_product_02_quantity),
	(v_bill_id, v_product_03_id, v_product_03_quantity, v_product_03_price*v_product_03_quantity);
	
	-- 4. Reducir el stock:
    UPDATE products
    SET stock = stock - v_product_01_quantity
    WHERE id = v_product_01_id;

    UPDATE products
    SET stock = stock - v_product_02_quantity
    WHERE id = v_product_02_id;

    UPDATE products
    SET stock = stock - v_product_03_quantity
    WHERE id = v_product_03_id;

	-- 5. Terminar la factura
	SELECT SUM(amount) INTO v_total_amount
	FROM "bill-product"
	WHERE bill_id = v_bill_id
	GROUP BY bill_id;

	UPDATE bills
	SET total_amount = v_total_amount
	WHERE id = v_bill_id;

	RAISE NOTICE 'Transacción finalizada.';
END $$;