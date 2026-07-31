SET search_path TO "Ejercicios_Transactions";

DO $$
DECLARE
    -- Definimos variables para almacenar datos durante la ejecución
    v_product_01_id INTEGER := 4;
	v_product_02_id INTEGER := 8;
	v_product_03_id INTEGER := 9;
	v_product_01_quantity INTEGER := 1;
	v_product_02_quantity INTEGER := 2;
	v_product_03_quantity INTEGER := 2;
	v_product_01_price REAL;
	v_product_02_price REAL;
	v_product_03_price REAL;
	v_available_stock INTEGER;
	v_buyer VARCHAR(50) := 'fluffy_cinnamoroll';
	v_user_id INTEGER;
	v_bill_id INTEGER;
	v_total_amount REAL;
	v_invoice_number VARCHAR(15) := 'INV-202607-1004';

BEGIN
    -- 1. Comprobar si hay existencias suficientes de cada uno de los productos dentro de la factura
    -- Verificación de existencias del primer producto
    SELECT stock INTO v_available_stock
    FROM products
    WHERE id = v_product_01_id;

    IF v_available_stock IS NULL OR v_available_stock < v_product_01_quantity THEN
      RAISE EXCEPTION 'No hay suficientes unidades del producto en el inventario';
    END IF;

	SELECT price INTO v_product_01_price
    FROM products
    WHERE id = v_product_01_id;
    -- Verificación de existencias del segundo producto
    SELECT stock INTO v_available_stock
    FROM products
    WHERE id = v_product_02_id;

    IF v_available_stock IS NULL OR v_available_stock < v_product_02_quantity THEN
      RAISE EXCEPTION 'No hay suficientes unidades del producto en el inventario';
    END IF;

	SELECT price INTO v_product_02_price
    FROM products
    WHERE id = v_product_02_id;
    -- Verificación de existencias del tercer producto
    SELECT stock INTO v_available_stock
    FROM products
    WHERE id = v_product_03_id;

    IF v_available_stock IS NULL OR v_available_stock < v_product_03_quantity THEN
      RAISE EXCEPTION 'No hay suficientes unidades del producto en el inventario';
    END IF;

	SELECT price INTO v_product_03_price
    FROM products
    WHERE id = v_product_03_id;

	-- 2. Confirmar que el usuario que realiza la compra existe en la DB
	SELECT id INTO v_user_id
	FROM users
	WHERE username = v_buyer;

	IF v_user_id IS NULL THEN
	  RAISE EXCEPTION 'El usuario no existe en la base de datos';
	END IF;
	
    -- 3. Insertar la factura con el usuario relacionado
    INSERT INTO bills (invoice_number, user_id)
    VALUES (v_invoice_number, v_user_id);

	SELECT id INTO v_bill_id
	FROM bills
	WHERE invoice_number = v_invoice_number;

	INSERT INTO "bill-product" (bill_id, product_id, quantity, amount)
	VALUES 
	(v_bill_id, v_product_01_id, v_product_01_quantity, v_product_01_price*v_product_01_quantity),
	(v_bill_id, v_product_02_id, v_product_02_quantity, v_product_02_price*v_product_02_quantity),
	(v_bill_id, v_product_03_id, v_product_03_quantity, v_product_03_price*v_product_03_quantity);

	SELECT SUM(amount) INTO v_total_amount
	FROM "bill-product"
	WHERE bill_id = v_bill_id
	GROUP BY bill_id;

	UPDATE bills
	SET total_amount = v_total_amount
	WHERE id = v_bill_id;
	
    -- 4. Reducir el stock de los productos según la cantidad comprada.
    UPDATE products
    SET stock = stock - v_product_01_quantity
    WHERE id = v_product_01_id;

	UPDATE products
    SET stock = stock - v_product_02_quantity
    WHERE id = v_product_02_id;

	UPDATE products
    SET stock = stock - v_product_03_quantity
    WHERE id = v_product_03_id;

	RAISE NOTICE 'Transacción finalizada.';
END $$;