from primer.models.common.identifier import Identifier

identifier = Identifier(
    namespace="ES.ES61.NGA",
    local_id="242130",
)

print(identifier)

print(identifier.namespace)

print(identifier.local_id)

print(identifier.full_id)