---
search:
  boost: 10.0
---

# Class: SecretText 


_Information about secret text used in the process of authenticating the_

_individual as an user accessing a system, e.g., when recovering a lost_

_password_



<div data-search-exclude markdown="1">



URI: [pd:SecretText](https://w3id.org/lmodel/dpv/pd/SecretText)





```mermaid
 classDiagram
    class SecretText
    click SecretText href "../SecretText/"
      Authenticating <|-- SecretText
        click Authenticating href "../Authenticating/"
      
      
```





## Inheritance
* [Internal](Internal.md)
    * [Authenticating](Authenticating.md)
        * **SecretText**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:SecretText](https://w3id.org/lmodel/dpv/pd/SecretText) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Secret Text




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#SecretText |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:SecretText |
| native | pd:SecretText |
| exact | dpv_pd:SecretText, dpv_pd_owl:SecretText |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SecretText
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#SecretText
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about secret text used in the process of authenticating
  the

  individual as an user accessing a system, e.g., when recovering a lost

  password'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Secret Text
exact_mappings:
- dpv_pd:SecretText
- dpv_pd_owl:SecretText
is_a: Authenticating
class_uri: pd:SecretText

```
</details>

### Induced

<details>
```yaml
name: SecretText
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#SecretText
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about secret text used in the process of authenticating
  the

  individual as an user accessing a system, e.g., when recovering a lost

  password'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Secret Text
exact_mappings:
- dpv_pd:SecretText
- dpv_pd_owl:SecretText
is_a: Authenticating
class_uri: pd:SecretText

```
</details></div>