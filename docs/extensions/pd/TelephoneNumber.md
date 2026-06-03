---
search:
  boost: 10.0
---

# Class: TelephoneNumber 


_Information about telephone number_



<div data-search-exclude markdown="1">



URI: [pd:TelephoneNumber](https://w3id.org/lmodel/dpv/pd/TelephoneNumber)





```mermaid
 classDiagram
    class TelephoneNumber
    click TelephoneNumber href "../TelephoneNumber/"
      Contact <|-- TelephoneNumber
        click Contact href "../Contact/"
      
      
```





## Inheritance
* [Tracking](Tracking.md)
    * [Contact](Contact.md)
        * **TelephoneNumber**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:TelephoneNumber](https://w3id.org/lmodel/dpv/pd/TelephoneNumber) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Telephone Number




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#TelephoneNumber |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:TelephoneNumber |
| native | pd:TelephoneNumber |
| exact | dpv_pd:TelephoneNumber, dpv_pd_owl:TelephoneNumber |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TelephoneNumber
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#TelephoneNumber
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about telephone number
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Telephone Number
exact_mappings:
- dpv_pd:TelephoneNumber
- dpv_pd_owl:TelephoneNumber
is_a: Contact
class_uri: pd:TelephoneNumber

```
</details>

### Induced

<details>
```yaml
name: TelephoneNumber
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#TelephoneNumber
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about telephone number
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Telephone Number
exact_mappings:
- dpv_pd:TelephoneNumber
- dpv_pd_owl:TelephoneNumber
is_a: Contact
class_uri: pd:TelephoneNumber

```
</details></div>