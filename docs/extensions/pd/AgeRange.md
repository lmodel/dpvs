---
search:
  boost: 10.0
---

# Class: AgeRange 


_Information about age range i.e. inexact age to some degree (i.e. some_

_years)_



<div data-search-exclude markdown="1">



URI: [pd:AgeRange](https://w3id.org/lmodel/dpv/pd/AgeRange)





```mermaid
 classDiagram
    class AgeRange
    click AgeRange href "../AgeRange/"
      Age <|-- AgeRange
        click Age href "../Age/"
      

      AgeRange <|-- AgeExact
        click AgeExact href "../AgeExact/"
      

      
```





## Inheritance
* [External](External.md)
    * [PhysicalCharacteristic](PhysicalCharacteristic.md)
        * [Age](Age.md)
            * **AgeRange**
                * [AgeExact](AgeExact.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:AgeRange](https://w3id.org/lmodel/dpv/pd/AgeRange) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Age Range




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#AgeRange |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:AgeRange |
| native | pd:AgeRange |
| exact | dpv_pd:AgeRange, dpv_pd_owl:AgeRange |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AgeRange
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#AgeRange
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about age range i.e. inexact age to some degree (i.e. some

  years)'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Age Range
exact_mappings:
- dpv_pd:AgeRange
- dpv_pd_owl:AgeRange
is_a: Age
class_uri: pd:AgeRange

```
</details>

### Induced

<details>
```yaml
name: AgeRange
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#AgeRange
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about age range i.e. inexact age to some degree (i.e. some

  years)'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Age Range
exact_mappings:
- dpv_pd:AgeRange
- dpv_pd_owl:AgeRange
is_a: Age
class_uri: pd:AgeRange

```
</details></div>