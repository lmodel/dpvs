---
search:
  boost: 10.0
---

# Class: DpvAuditor 


_Actor that audits Technology for conformance to policies, standards, or_

_legal requirements_



<div data-search-exclude markdown="1">



URI: [tech:Auditor](https://w3id.org/lmodel/dpv/tech/Auditor)





```mermaid
 classDiagram
    class DpvAuditor
    click DpvAuditor href "../DpvAuditor/"
      Actor <|-- DpvAuditor
        click Actor href "../Actor/"
      Partner <|-- DpvAuditor
        click Partner href "../Partner/"
      
      
```





## Inheritance
* [Actor](Actor.md)
    * [Partner](Partner.md)
        * **DpvAuditor** [ [Actor](Actor.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Auditor](https://w3id.org/lmodel/dpv/tech/Auditor) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Auditor




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 |
| upstream_iri | https://w3id.org/dpv/tech/owl#Auditor |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Auditor |
| native | tech:DpvAuditor |
| exact | dpv_tech:Auditor, dpv_tech_owl:Auditor |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DpvAuditor
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Auditor
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Actor that audits Technology for conformance to policies, standards,
  or

  legal requirements'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Auditor
exact_mappings:
- dpv_tech:Auditor
- dpv_tech_owl:Auditor
is_a: Partner
mixins:
- Actor
class_uri: tech:Auditor

```
</details>

### Induced

<details>
```yaml
name: DpvAuditor
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Auditor
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Actor that audits Technology for conformance to policies, standards,
  or

  legal requirements'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Auditor
exact_mappings:
- dpv_tech:Auditor
- dpv_tech_owl:Auditor
is_a: Partner
mixins:
- Actor
class_uri: tech:Auditor

```
</details></div>