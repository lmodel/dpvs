---
search:
  boost: 10.0
---

# Class: PublicSecurityImpaired 


_Justification that the process could not be fulfilled or was not_

_successful because it would interfere with necessary tasks to safeguard_

_public security_



<div data-search-exclude markdown="1">



URI: [justifications:PublicSecurityImpaired](https://w3id.org/lmodel/dpv/justifications/PublicSecurityImpaired)





```mermaid
 classDiagram
    class PublicSecurityImpaired
    click PublicSecurityImpaired href "../PublicSecurityImpaired/"
      SecurityImpaired <|-- PublicSecurityImpaired
        click SecurityImpaired href "../SecurityImpaired/"
      LegalProcessImpaired <|-- PublicSecurityImpaired
        click LegalProcessImpaired href "../LegalProcessImpaired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * **PublicSecurityImpaired** [ [SecurityImpaired](SecurityImpaired.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:PublicSecurityImpaired](https://w3id.org/lmodel/dpv/justifications/PublicSecurityImpaired) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Public Security Impaired




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#PublicSecurityImpaired |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:PublicSecurityImpaired |
| native | justifications:PublicSecurityImpaired |
| exact | dpv_justifications:PublicSecurityImpaired, dpv_justifications_owl:PublicSecurityImpaired |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PublicSecurityImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#PublicSecurityImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with necessary tasks to safeguard

  public security'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Public Security Impaired
exact_mappings:
- dpv_justifications:PublicSecurityImpaired
- dpv_justifications_owl:PublicSecurityImpaired
is_a: LegalProcessImpaired
mixins:
- SecurityImpaired
class_uri: justifications:PublicSecurityImpaired

```
</details>

### Induced

<details>
```yaml
name: PublicSecurityImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#PublicSecurityImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with necessary tasks to safeguard

  public security'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Public Security Impaired
exact_mappings:
- dpv_justifications:PublicSecurityImpaired
- dpv_justifications_owl:PublicSecurityImpaired
is_a: LegalProcessImpaired
mixins:
- SecurityImpaired
class_uri: justifications:PublicSecurityImpaired

```
</details></div>