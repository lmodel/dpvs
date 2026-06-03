---
search:
  boost: 10.0
---

# Class: PINCode 


_Information about personal identification number (PIN), which is usually_

_used in the process of authenticating the individual as an user_

_accessing a system_



<div data-search-exclude markdown="1">



URI: [pd:PINCode](https://w3id.org/lmodel/dpv/pd/PINCode)





```mermaid
 classDiagram
    class PINCode
    click PINCode href "../PINCode/"
      Authenticating <|-- PINCode
        click Authenticating href "../Authenticating/"
      
      
```





## Inheritance
* [Internal](Internal.md)
    * [Authenticating](Authenticating.md)
        * **PINCode**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:PINCode](https://w3id.org/lmodel/dpv/pd/PINCode) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* PIN Code




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#PINCode |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:PINCode |
| native | pd:PINCode |
| exact | dpv_pd:PINCode, dpv_pd_owl:PINCode |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PINCode
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PINCode
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about personal identification number (PIN), which is usually

  used in the process of authenticating the individual as an user

  accessing a system'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- PIN Code
exact_mappings:
- dpv_pd:PINCode
- dpv_pd_owl:PINCode
is_a: Authenticating
class_uri: pd:PINCode

```
</details>

### Induced

<details>
```yaml
name: PINCode
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PINCode
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about personal identification number (PIN), which is usually

  used in the process of authenticating the individual as an user

  accessing a system'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- PIN Code
exact_mappings:
- dpv_pd:PINCode
- dpv_pd_owl:PINCode
is_a: Authenticating
class_uri: pd:PINCode

```
</details></div>