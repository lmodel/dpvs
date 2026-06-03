---
search:
  boost: 10.0
---

# Class: Authenticating 


_Information about authentication and information used for authenticating_



<div data-search-exclude markdown="1">



URI: [pd:Authenticating](https://w3id.org/lmodel/dpv/pd/Authenticating)





```mermaid
 classDiagram
    class Authenticating
    click Authenticating href "../Authenticating/"
      Internal <|-- Authenticating
        click Internal href "../Internal/"
      

      Authenticating <|-- PINCode
        click PINCode href "../PINCode/"
      Authenticating <|-- Password
        click Password href "../Password/"
      Authenticating <|-- SecretText
        click SecretText href "../SecretText/"
      

      
```





## Inheritance
* [Internal](Internal.md)
    * **Authenticating**
        * [PINCode](PINCode.md)
        * [Password](Password.md)
        * [SecretText](SecretText.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Authenticating](https://w3id.org/lmodel/dpv/pd/Authenticating) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Authenticating




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Authenticating |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Authenticating |
| native | pd:Authenticating |
| exact | dpv_pd:Authenticating, dpv_pd_owl:Authenticating |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Authenticating
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Authenticating
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about authentication and information used for authenticating
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Authenticating
exact_mappings:
- dpv_pd:Authenticating
- dpv_pd_owl:Authenticating
is_a: Internal
class_uri: pd:Authenticating

```
</details>

### Induced

<details>
```yaml
name: Authenticating
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Authenticating
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about authentication and information used for authenticating
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Authenticating
exact_mappings:
- dpv_pd:Authenticating
- dpv_pd_owl:Authenticating
is_a: Internal
class_uri: pd:Authenticating

```
</details></div>