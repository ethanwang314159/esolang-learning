# excon_interpreter.rb

def interpret_EXCON(source)
  pool = %w[0 0 0 0 0 0 0 0]
  pointer = 7

  for i in 0..source.length
    case source[i..i]
    when ":" then pool = %w[0 0 0 0 0 0 0 0]; pointer = 7
    when "^" then pool[pointer] = pool[pointer] == '1' ? '0' : '1'
    when "<" then pointer -= 1
    when "!" then print pool.join.to_i(2).chr
    end
  end
end

if ARGV.length == 1
  source = File.read(ARGV[0])
  interpret_EXCON(source)
else
  puts "Usage: ruby excon_interpreter.rb [filepath]"
end
