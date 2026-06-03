---
search:
  boost: 10.0
---

# Class: NationalSecurityImpaired 


_Justification that the process could not be fulfilled or was not_

_successful because it would interfere with necessary tasks to safeguard_

_national security_



<div data-search-exclude markdown="1">



URI: [justifications:NationalSecurityImpaired](https://w3id.org/lmodel/dpv/justifications/NationalSecurityImpaired)





```mermaid
 classDiagram
    class NationalSecurityImpaired
    click NationalSecurityImpaired href "../NationalSecurityImpaired/"
      SecurityImpaired <|-- NationalSecurityImpaired
        click SecurityImpaired href "../SecurityImpaired/"
      LegalProcessImpaired <|-- NationalSecurityImpaired
        click LegalProcessImpaired href "../LegalProcessImpaired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * **NationalSecurityImpaired** [ [SecurityImpaired](SecurityImpaired.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:NationalSecurityImpaired](https://w3id.org/lmodel/dpv/justifications/NationalSecurityImpaired) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* National Security Impaired




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#NationalSecurityImpaired |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:NationalSecurityImpaired |
| native | justifications:NationalSecurityImpaired |
| exact | dpv_justifications:NationalSecurityImpaired, dpv_justifications_owl:NationalSecurityImpaired |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NationalSecurityImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#NationalSecurityImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with necessary tasks to safeguard

  national security'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- National Security Impaired
exact_mappings:
- dpv_justifications:NationalSecurityImpaired
- dpv_justifications_owl:NationalSecurityImpaired
is_a: LegalProcessImpaired
mixins:
- SecurityImpaired
class_uri: justifications:NationalSecurityImpaired

```
</details>

### Induced

<details>
```yaml
name: NationalSecurityImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#NationalSecurityImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with necessary tasks to safeguard

  national security'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- National Security Impaired
exact_mappings:
- dpv_justifications:NationalSecurityImpaired
- dpv_justifications_owl:NationalSecurityImpaired
is_a: LegalProcessImpaired
mixins:
- SecurityImpaired
class_uri: justifications:NationalSecurityImpaired

```
</details></div>