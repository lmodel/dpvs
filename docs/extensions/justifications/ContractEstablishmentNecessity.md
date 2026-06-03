---
search:
  boost: 10.0
---

# Class: ContractEstablishmentNecessity 


_Justification that the process could not be fulfilled or was not_

_successful because it is necessary for entering into a contract_



<div data-search-exclude markdown="1">



URI: [justifications:ContractEstablishmentNecessity](https://w3id.org/lmodel/dpv/justifications/ContractEstablishmentNecessity)





```mermaid
 classDiagram
    class ContractEstablishmentNecessity
    click ContractEstablishmentNecessity href "../ContractEstablishmentNecessity/"
      LegalProcessImpaired <|-- ContractEstablishmentNecessity
        click LegalProcessImpaired href "../LegalProcessImpaired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * **ContractEstablishmentNecessity**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:ContractEstablishmentNecessity](https://w3id.org/lmodel/dpv/justifications/ContractEstablishmentNecessity) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Contract Establishment Necessity




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#ContractEstablishmentNecessity |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:ContractEstablishmentNecessity |
| native | justifications:ContractEstablishmentNecessity |
| exact | dpv_justifications:ContractEstablishmentNecessity, dpv_justifications_owl:ContractEstablishmentNecessity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ContractEstablishmentNecessity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#ContractEstablishmentNecessity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it is necessary for entering into a contract'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Contract Establishment Necessity
exact_mappings:
- dpv_justifications:ContractEstablishmentNecessity
- dpv_justifications_owl:ContractEstablishmentNecessity
is_a: LegalProcessImpaired
class_uri: justifications:ContractEstablishmentNecessity

```
</details>

### Induced

<details>
```yaml
name: ContractEstablishmentNecessity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#ContractEstablishmentNecessity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it is necessary for entering into a contract'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Contract Establishment Necessity
exact_mappings:
- dpv_justifications:ContractEstablishmentNecessity
- dpv_justifications_owl:ContractEstablishmentNecessity
is_a: LegalProcessImpaired
class_uri: justifications:ContractEstablishmentNecessity

```
</details></div>